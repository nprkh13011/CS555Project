import Login from "../components/Login"
import {fireEvent, getByText, render, screen} from "@testing-library/react";
import '@testing-library/jest-dom';
import { jest } from "@jest/globals";
import userEvent from '@testing-library/user-event';

it("should have email and password fields, along with a submit button", () => {
    render(<Login/>) 
    //from the login form - used Testing Library documentation
    const email = screen.getByLabelText("Email");
    const password = screen.getByLabelText("Password");
    const submit = screen.getByText(/submit/i);

    expect(email).toBeInTheDocument();
    expect(password).toBeInTheDocument();
    expect(submit).toBeInTheDocument();

});

it("should allow the user to submit/sign in to the application", () => {
    const submit = jest.fn();
    render(<Login submit={submit}/>);

    const email = screen.getByLabelText("Email");
    const password = screen.getByLabelText("Password");
    const submitButton = screen.getByText(/submit/i);

    userEvent.type(email, "testing@test.com");
    userEvent.type(password, "testing123");
    userEvent.click(submitButton); //user clicks the button

    // button should take in email and password
    expect(submit).toHaveBeenCalledWith({email: "testing@test.com", password: "testing123"});
});

it("should correctly take in login information once inputted", () => {
    
    render(<Login/>);

    const email = screen.getByLabelText("Email");
    const password = screen.getByLabelText("Password");

    userEvent.type(email, "testing@test.com");
    userEvent.type(password, "testing123");

    expect(email).toHaveValue("testing@test.com");
    expect(password).toHaveValue("testing123");


});