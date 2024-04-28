import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import resultsScores from "./LieTest.js";

const ResultsPage = (props) => {
  const navigate = useNavigate();
  const truthScore = resultsScores;
  var r = [truthScore, 17 - truthScore];
  useEffect(() => {
    console.log(props.resultsScores);
  }, [props.resultsScores]);
  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div
        className="peach p-3 rounded w-50 h-70 text-center teal"
        style={{ width: "50%" }}
      >
        <h1 className="mb-4">Thank you for using our application!</h1>
        <p>
          We have compiled your results below including how many questions you
          answered truthfully and untruthfully and your professor rankings.
        </p>
        <div class="row">
          <div class="col">
            <b>Questions answered truthfully: {props.resultsScores}</b>
          </div>
          <div class="col">
            <b>Questions answered untruthfully: {17 - props.resultsScores}</b>
          </div>
        </div>
        <div className="mt-3 d-flex justify-content-between">
          <button
            className="btn btn-success rounded"
            onClick={() => navigate("/home")}
          >
            Go Home
          </button>
          <button
            className="btn btn-success rounded"
            onClick={() => navigate("/rankings")}
          >
            See Professor Rankings
          </button>
          <button
            className="btn btn-danger rounded"
            onClick={() => navigate("/logout")}
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResultsPage;
