import React, {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom'
import Logo from "../img/FibFinders_Logo.png";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const [auth, setAuth] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:3001/login", { email, password })
      .then((response) => {
        if (response.data.exists) {
          navigate("/home", { state: { emailid: email } });
        } else {
          setAuth(true);
        }
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div
        className="peach p-3 rounded w-50 h-70 text-center teal"
        style={{ width: "35%" }}
      >
        <h1>Login</h1>
        <img
          src={Logo}
          alt="FibFinders Logo"
          className="mb-3 rounded"
          style={{ maxWidth: "150px" }}
        />
        {auth && (
          <p className="black text-danger">
            Either username or password is incorrect.
          </p>
        )}
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label
              htmlFor="email"
              style={{
                textAlign: "left",
                width: "100%",
                display: "inline-block",
              }}
              className="form-label"
            >
              <strong>Email</strong>
            </label>
            <input
              type="text"
              className="form-control rounded-0"
              name="email"
              placeholder="Enter Email Address"
              value={email}
              id="email"
              required
              onChange={(e) => setEmail(e.target.value)}
              autoComplete="off"
            />
          </div>
          <div className="mb-4">
            <label
              htmlFor="password"
              style={{
                textAlign: "left",
                width: "100%",
                display: "inline-block",
              }}
              className="form-label"
            >
              <strong>Password</strong>
            </label>
            <input
              type="password"
              className="form-control rounded-0"
              name="password"
              required
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter Password"
            />
          </div>
          <button type="submit" className="btn btn-success rounded-10 ">
            Sign In
          </button>
          <br />
          Don't Have Account? <Link to="/signup">Register Here</Link>
        </form>
      </div>
    </div>
  );
};

export default Login;