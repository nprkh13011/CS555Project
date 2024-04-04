import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

import {ProgressBar} from 'react-bootstrap';


const Progress = ({ percentage }) => {
  return (
    <div className="progress-bar">
      <ProgressBar striped  now={percentage} style={{ width: 400 }}/>
    </div>
  )
}

export default Progress