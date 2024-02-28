// import { useState } from 'react'
// import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Link } from 'react-router-dom'

const SignUp = () => {
  // const [count, setCount] = useState(0)

  return (
    <div className="d-flex justify-content-center align-items-center bg-secondary vh-100">
      <div className="bg-white p-3 rounded w-25">
        <h1>Sign Up</h1>
        <form>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">Email</label>
            <input type="text" className="form-control rounded-0" name="email" placeholder='Enter Email Address' autoComplete='off' />
          </div>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">Password</label>
            <input type="password" className="form-control rounded-0" name="password" placeholder='Enter Password' />
          </div>
          <button type="submit" className="btn btn-success w-100 rounded-0">Sign Up</button>
          <p>Already have an account?</p>
          <Link to="/login" className="btn btn-default borderbg-light rounded-0 text-decoration-none rounded-0">Login</Link>
        </form>
      </div>
    </div>
  ); 
}

export default SignUp;