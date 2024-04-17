import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Pagination} from '@mui/material';
import {ProgressBar} from 'react-bootstrap';


const Progress = () => {
  const [progress, setProgress] = useState(1)
  const handleChange = (e, val) => {
    setProgress(val);
  }
  
  return (
    <div >
      <Pagination hidePrevButton count={17} page={progress} onChange={(e, val) => setProgress(val)} color="primary" variant="outlined" data-testid="pagination"/>
      
      {/* <ProgressBar striped animated now={progress} style={{ width: 500 }}/>
      <button type="submit" onClick={handleProgress} className="btn btn-secondary w-20 mt-5 rounded-10 ">Next</button> */}
    </div>
  )
}

export default Progress