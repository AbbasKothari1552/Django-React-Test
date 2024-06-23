import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/form.css";
import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [first_name, setfirst_name] = useState("");
  const [last_name, setlast_name] = useState("");
  const [confirmpassword, setconfirmpassword] = useState("");

  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const name = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();

    if (method === "register" && password !== confirmpassword) {
      alert("Passwords do not match!");
      setLoading(false);
      return;
    }

    try {
      const payload = {
        password,
        email,
        ...(method === "register" && {
            confirmpassword:confirmpassword,
          first_name: first_name,
          last_name: last_name,
        }),
      };

      const res = await api.post(route, payload);

      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        navigate("/");
      } else {
        navigate("/login");
      }
    } catch (error) {
      alert(error.response?.data?.message || error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>{name}</h1>
      {method === "register" && (
        <>
          <input
            className="form-input"
            type="text"
            value={first_name}
            onChange={(e) => setfirst_name(e.target.value)}
            placeholder="First Name"
          />
          <input
            className="form-input"
            type="text"
            value={last_name}
            onChange={(e) => setlast_name(e.target.value)}
            placeholder="Last Name"
          />
        </>
      )}
      <input
        className="form-input"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        className="form-input"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      {method === "register" && (
        <input
          className="form-input"
          type="password"
          value={confirmpassword}
          onChange={(e) => setconfirmpassword(e.target.value)}
          placeholder="Re-enter Password"
        />
      )}
      {loading && <LoadingIndicator />}
      <button className="form-button" type="submit">
        {name}
      </button>
    </form>
  );
}

export default Form;
