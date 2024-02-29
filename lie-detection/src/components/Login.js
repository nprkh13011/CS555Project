import React, {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'

const Login = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div className="bg-white p-5 rounded border " style = {{width:'35%'}}>
        <h1 className="mb-4">Login</h1>
        <form>
          <div className="mb-3">
            <label htmlFor="email" style={{ textAlign: 'left', width: '100%', display: 'inline-block' }} className="form-label">Email</label>
            <input 
              type="text" 
              className="form-control rounded-0" 
              name="email" 
              placeholder='Enter Email Address' 
              value = {email}
              onChange = {(e) => setEmail(e.target.value)}
              autoComplete='off' />
          </div>
          <div className="mb-4">
            <label htmlFor="email" style={{ textAlign: 'left', width: '100%', display: 'inline-block' }} className="form-label">Password</label>
            <input 
              type="password" 
              className="form-control rounded-0" 
              name="password" 
              value = {password}
              onChange = {(e) => setPassword(e.target.value)}
              placeholder='Enter Password' />
          </div>
          <button type="submit" className="btn btn-secondary w-50 rounded-10 ">Login</button>
          
        </form>
      </div>
    </div>
  )
}

export default Login