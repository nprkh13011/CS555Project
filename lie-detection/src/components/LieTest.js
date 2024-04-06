import React, { useState, Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import { Button } from 'bootstrap'
import {Navigate} from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import Swal from 'sweetalert2';
import Progress from './Progress.js';

const About = () => {
    const navigate = useNavigate()
}

class LieTest extends Component {
    

    constructor(props) {
        super(props)

        this.onClickForward = this.onClickForward.bind(this)
        this.returnHome = this.returnHome.bind(this)

        // const img1 = require('./images/image1.png');
        // const img2 = require('./images/image2.png');
        // const img3 = require('./images/image3.png');
        // const img4 = require('./images/image4.png');
        // const img5 = require('./images/image5.png');
        // const img6 = require('./images/image6.png');
        // const img7 = require('./images/image7.png');
        // const img8 = require('./images/image8.png');
        // const img9 = require('./images/image9.png');
        // const img10 = require('./images/image10.png');
        // const img11 = require('./images/image11.png');
        // const img12 = require('./images/image12.png');
        // const img13 = require('./images/image13.png');
        // const img14 = require('./images/image14.png');
        // const img15 = require('./images/image15.png');
        // const img16 = require('./images/image16.png');
        // const img17 = require('./images/image17.png');
        
        this.state = {
            index: 0,
            // imgList: [img1, img2, img3,img4,img5,img6, img7,
            //           img8, img9, img10, img11, img12, img13,
            //           img14, img15, img16, img17],
            endOfTest: false
        }
    }
    
    onClickForward() {
        //if at the end of the test
        if (this.state.index + 1 === this.state.imgList.length){
            this.setState({
                index: this.state.imgList.length,
                endOfTest: true
            })
        } else { // if we don't reach end of the test
            this.setState({
                index: this.state.index + 1
            })
        }
    }

    returnHome() {

        Swal.fire({
            title: "Are you sure?",
            text: "You won't be able to pick up where you left off",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Yes, exit test"
          }).then((result) => {
            if (result.isConfirmed) {
                this.setState({
                    index: this.state.imgList.length,
                    endOfTest: true
                })    
            }
          });
    }
   render() {

        return (
            <div>
                <div className="d-flex justify-content-center align-items-center vw-100 vh-100">
                    <Progress />
                {/* <div className="bg-white p-5 rounded border " style = {{width:'50%'}}>
                    <h1 className="mb-4">Lie Test</h1>
                    <h2 className='lietest'>Question {this.state.index + 1}</h2>
                    <img src = {this.state.imgList[this.state.index]}/><br/>
                  {this.state.endOfTest && <Navigate to="/home"/> } 
                    <button onClick={this.onClickForward}>Yes</button><br/>
                    <button onClick={this.onClickForward}>No</button><br/>
                    <button onClick={this.returnHome}>End Test</button>
                </div> */}
                </div>
            </div>
        )
    }

}
export default LieTest;