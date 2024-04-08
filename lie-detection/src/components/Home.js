import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import Logo from '../img/FibFinders_Logo.png';

const Home = () => {
    const navigate = useNavigate()
    
    return (
        <div className="d-flex justify-content-center align-items-center bg-white vh-100">
            <div className="peach p-3 rounded w-50 h-70 text-center teal">
                <img src={Logo} alt="FibFinders Logo" className="mb-3 rounded" style={{ maxWidth: "150px" }} />
            <div className="mb-3">
            <button className="btn btn-primary rounded" onClick={() => navigate('/rankings')}>View Professor Ratings</button>
            </div>
            <div className="mb-3">
            <button className="btn btn-success rounded" onClick={() => navigate('/instructions')}>Start Test</button>
            </div>
            <div className="mb-3">
            <button className="btn btn-danger rounded " onClick={() => navigate('/logout')}>Logout</button>
            </div>
        </div>
        </div>
    )
}

export default Home;