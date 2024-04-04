import React, {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom'


const Login = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate();
  const [auth, setAuth] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:3001/login', { email, password })
      .then(response => {
        if (response.data.exists) {
          navigate('/home', {state: {emailid: email}});
        } else {
          setAuth(true)
        }
      })
      .catch(err => console.log(err));

  }
  
  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div className="bg-white p-5 rounded border " style = {{width:'35%'}}>
        <h1 className="mb-4">Login</h1>
        {auth && <p className="text-danger">Either username or password is incorrect.</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="email" style={{ textAlign: 'left', width: '100%', display: 'inline-block' }} className="form-label">Email</label>
            <input 
              type="text" 
              className="form-control rounded-0" 
              name="email" 
              placeholder='Enter Email Address' 
              value = {email}
              id="email"
              required
              onChange = {(e) => setEmail(e.target.value)}
              autoComplete='off' />
          </div>
          <div className="mb-4">
            <label htmlFor="password" style={{ textAlign: 'left', width: '100%', display: 'inline-block' }} className="form-label">Password</label>
            <input 
              type="password" 
              className="form-control rounded-0" 
              name="password" 
              required
              id="password"
              value = {password}
              onChange = {(e) => setPassword(e.target.value)}
              placeholder='Enter Password' />
          </div>
          <button type="submit" className="btn btn-secondary w-50 rounded-10 ">Submit</button>
          <br/>
          <Link to='/signup'>Click Here to Register</Link>
        </form>
      </div>
    </div>
  )
}

export default Login;