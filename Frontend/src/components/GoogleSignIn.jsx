import React from "react";
import { GoogleLogin } from '@react-oauth/google';

const GoogleSignIn = ({ handleGoogleSuccess, handleGoogleFailure }) => {
  return (
    <GoogleLogin
      onSuccess={credentialResponse => handleGoogleSuccess(credentialResponse)}
      onError={() => handleGoogleFailure()}
    />
  );
};

export default GoogleSignIn;
