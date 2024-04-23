import React, { useState, Component, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import { Button } from 'bootstrap'
import { Navigate } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import Swal from 'sweetalert2';
import Progress from './Progress.js';
import img1 from './images/image1.png';
import img2 from './images/image2.png';
import img3 from './images/image3.png';
import img4 from './images/image4.png';
import img5 from './images/image5.png';
import img6 from './images/image6.png';
import img7 from './images/image7.png';
import img8 from './images/image8.png';
import img9 from './images/image9.png';
import img10 from './images/image10.png';
import img11 from './images/image11.png';
import img12 from './images/image12.png';
import img13 from './images/image13.png';
import img14 from './images/image14.png';
import img15 from './images/image15.png';
import img16 from './images/image16.png';
import img17 from './images/image17.png';

class LieTest extends Component {


    constructor(props) {
        super(props)

        this.onClickForward = this.onClickForward.bind(this)
        this.returnHome = this.returnHome.bind(this)


        this.state = {
            index: 0,
            imgList: [img1, img2, img3, img4, img5, img6,
                img7, img8, img9, img10, img11, img12,
                img13, img14, img15, img16, img17],
            endOfTest: false,
            redirectToHome: false
        }
    }

    onClickForward() {
        //if at the end of the test
        if (this.state.index + 1 === this.state.imgList.length) {
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
            title: "Are You Sure?",
            text: "You Won't Be Able to Pick Up Where You Left Off",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Yes, Restart Test"
        }).then((result) => {
            if (result.isConfirmed) {
                this.setState({
                    redirectToHome: true
                });
            }
        });
    }

    handleProgressChange = (value) => {
        this.setState({
            index: value - 1
        });
    };

    render() {

        return (
          <div className="d-flex justify-content-center align-items-center vh-100">
            <div className="peach-container p-3 rounded text-center">
              <div className="progress-bar-container">
                <Progress
                  style={{ marginTop: "50px", marginBottom: "50px" }}
                  current={this.state.index + 1}
                  onChange={this.handleProgressChange}
                />
              </div>
              <div className="white-container p-3 m-2 rounded text-center">
                <h1 className="lietest">
                  Have you taken a class with this professor?
                </h1>
                <div className="image-container my-4">
                  <img src={this.state.imgList[this.state.index]} />
                </div>
                <div className="button-container d-flex justify-content-between my-3">
                  {this.state.endOfTest && <Navigate to="/results" />}
                  <button
                    className="btn btn-primary rounded mx-2"
                    onClick={this.onClickForward}
                  >
                    Yes
                  </button>

                  <button
                    className="btn btn-primary rounded mx-2"
                    onClick={this.onClickForward}
                  >
                    No
                  </button>
                </div>
                <button
                  className="btn btn-danger rounded"
                  onClick={this.returnHome}
                  style={{ marginTop: "30px" }}
                >
                  Restart Test
                </button>
              </div>
            </div>
            <div className="d-flex justify-content-center"></div>
            {this.state.redirectToHome && <Navigate to="/home" />}
          </div>
        );
    }
}
export default LieTest;
