import React, {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Link } from 'react-router-dom'

const Logout = () => {
  return (
    // div tags classname are for UI purposes
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div className="bg-white p-5 rounded border " style = {{width:'35%'}}>
        <h1 className="mb-4">Logout</h1>
        <h2>You are officially logged out!</h2>
        <Link to="/login">Sign Back In!</Link>
      </div>
    </div>
  )
}

export default Logout;