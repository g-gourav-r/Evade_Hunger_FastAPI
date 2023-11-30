import React, { useState } from 'react';
import Axios from 'axios';
import './LoginSignUp.css';

const LoginSignUp = () => {
  const apiUrlSignup = 'http://127.0.0.1:8000/signup';
  const apiUrlLogin = 'http://127.0.0.1:8000/login';

  const [data, setData] = useState({
    name: '',
    email: '',
    password: '',
  });

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setData((prevData) => ({
      ...prevData,
      [id]: value,
    }));
  };

  const handleSignUp = async (e) => {
    e.preventDefault();

    try {
      const response = await Axios.post(apiUrlSignup, data);
      console.log(response.data); // Handle response as needed
    } catch (error) {
      console.error('Error occurred while signing up', error);
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await Axios.post(apiUrlLogin, data);
      console.log(response.data); // Handle response as needed
    } catch (error) {
      console.error('Error occurred while logging in', error);
    }
  };

  return (
    <div className="main">
      <input type="checkbox" id="chk" aria-hidden="true" />

      <div className="signup">
        <form onSubmit={handleSignUp}>
          <label htmlFor="chk" aria-hidden="true">
            Sign up
          </label>
          <input
            onChange={handleInputChange}
            id="name"
            value={data.name}
            type="text"
            name="txt"
            placeholder="User name"
            required
          />
          <input
            onChange={handleInputChange}
            id="email"
            value={data.email}
            type="email"
            name="email"
            placeholder="Email"
            required
          />
          <input
            onChange={handleInputChange}
            id="password"
            value={data.password}
            type="password"
            name="pswd"
            placeholder="Password"
            required
          />
          <button type="submit">Sign up</button>
        </form>
      </div>

      <div className="login">
        <form onSubmit={handleLogin}>
          <label htmlFor="chk" aria-hidden="true">
            Login
          </label>
          <input
            type="email"
            name="email"
            placeholder="Email"
            required
          />
          <input
            type="password"
            name="pswd"
            placeholder="Password"
            required
          />
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
};

export default LoginSignUp;
