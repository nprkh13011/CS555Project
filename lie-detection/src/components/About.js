import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import Logo from '../img/FibFinders_Logo.png';

const About = () => {
    const navigate = useNavigate()
    
    return (
        <div className="d-flex justify-content-center align-items-center bg-white vh-100">
            <div className="peach p-3 rounded w-50 h-70 text-center teal">
            <img src={Logo} alt="FibFinders Logo" className="mb-3 rounded" style={{ maxWidth: "150px" }} />
            <h1>Welcome to FibFinders!</h1>
            <h3 className="h-15"> Through this application, you can determine if you have taken a certain professor before and recommend the class to other users. Through the analysis of your EEG waves, we can see if you're being truthful or not, affecting the recommendation rate of each professor.</h3>
            <div className="mb-3">
            <button className="btn btn-primary rounded" onClick={() => navigate('/signup')}>Sign Up</button>
            </div>
            <div className="mb-3">
            <button className="btn btn-primary rounded" onClick={() => navigate('/login')}>Login</button>
            </div>
        </div>
        </div>
    )
}

export default About;