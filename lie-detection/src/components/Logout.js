import React, {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Link } from 'react-router-dom'

const Logout = () => {
  return (
    // div tags classname are for UI purposes
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div
        className="peach p-3 rounded w-50 h-70 text-center"
        style={{ width: "50%" }}
      >
        <h1 className="mb-4">Logout</h1>
        <div className="bg-white p-3 rounded text-center">
          <h2>You are officially logged out!</h2>
        </div>
        <br />
        <Link to="/login">Sign Back In!</Link>
      </div>
    </div>
  );
};

export default Logout;