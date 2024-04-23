import { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import { Link, useNavigate } from 'react-router-dom'
import Logo from "../img/FibFinders_Logo.png";

const SignUp = () => {
  const [name, setName] = useState();
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const navigate = useNavigate();
  const [error, setError] = useState();
  const [emailExists, setEmailExists] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name || !email || !password) {
      throw new Error("All fields are required");
    }

    axios
      .post("http://localhost:3001/check-email", { email })
      .then((response) => {
        if (response.data.exists) {
          setError("Email already exists");
          setEmailExists(true);
        } else {
          // If email does not exist, proceed with signup
          axios
            .post("http://localhost:3001/signup", { name, email, password })
            .then((result) => {
              console.log(result);
              navigate("/login");
            })
            .catch((err) => console.log(err));
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
        <h1>Register</h1>
        <img
          src={Logo}
          alt="FibFinders Logo"
          className="mb-3 rounded"
          style={{ maxWidth: "150px" }}
        />
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label
              htmlFor="name"
              style={{
                textAlign: "left",
                width: "100%",
                display: "inline-block",
              }}
            >
              <strong>Name</strong>
            </label>
            <input
              type="text"
              className="form-control rounded-0"
              name="email"
              placeholder="Enter Name"
              autoComplete="off"
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label
              htmlFor="email"
              style={{
                textAlign: "left",
                width: "100%",
                display: "inline-block",
              }}
            >
              <strong>Email</strong>
            </label>
            <input
              type="text"
              className="form-control rounded-0"
              name="email"
              placeholder="Enter Email Address"
              autoComplete="off"
              onChange={(e) => setEmail(e.target.value)}
            />
            {emailExists && <p className="text-danger">Email already exists</p>}
          </div>
          <div className="mb-3">
            <label
              htmlFor="password"
              style={{
                textAlign: "left",
                width: "100%",
                display: "inline-block",
              }}
            >
              <strong>Password</strong>
            </label>
            <input
              type="password"
              className="form-control rounded-0"
              name="password"
              placeholder="Enter Password"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type="submit" className="btn btn-success rounded">
            Sign Up
          </button>
          <br />
          Already have an account?<Link to="/login">Login Here</Link>
        </form>
      </div>
    </div>
  );
};

export default SignUp;