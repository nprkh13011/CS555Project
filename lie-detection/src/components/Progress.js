import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Pagination} from '@mui/material';
import {ProgressBar} from 'react-bootstrap';


const Progress = () => {
  const [progress, setProgress] = useState(0)
  // const handleProgress = (e) => {
  //   let num = progress
  //   num = num + 6
  //   if (num > 100){
  //     num = 100
  //   }
  //   setProgress(num)
  // }
  return (
    <div >
      <Pagination hidePrevButton count={17} color="primary" variant="outlined" />
      
      {/* <ProgressBar striped animated now={progress} style={{ width: 500 }}/>
      <button type="submit" onClick={handleProgress} className="btn btn-secondary w-20 mt-5 rounded-10 ">Next</button> */}
    </div>
  )
}

export default Progress