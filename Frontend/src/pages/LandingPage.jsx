import React from 'react'
import { Link } from 'react-router-dom';
function LandingPage() {
  return (
    <>
    
    <Link to="/register">
        <button>Register</button>
      </Link>
      <Link to="/login">
        <button>Login</button>
      </Link>
    
    
    </>
  )
}

export default LandingPage