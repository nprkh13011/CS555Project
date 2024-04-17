import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Pagination} from '@mui/material';
import {ProgressBar} from 'react-bootstrap';


const Progress = ({ current, onChange }) => {
  const handlePageChange = (event, value) => {
    onChange(value);
};
  
  return (
    <div >
      <Pagination size="lg" hidePrevButton count={17} page={current} onChange={handlePageChange} color="primary" variant="outlined" data-testid="pagination"/>
    </div>
  )
}

export default Progress