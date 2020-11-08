import React, { Component } from 'react'
import { Navbar,Nav} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';

export class Header extends Component{
    render(){
        return (
            <Navbar bg="light" variant="light" id="navBar">
                <Navbar.Brand href="search">트하!</Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="login" id="LoginButton">로그인</Nav.Link>
                    <Nav.Link href="signup" id="SignupButton">회원가입</Nav.Link>
                </Nav>
            </Navbar>
        );
    }
}

export default Header;