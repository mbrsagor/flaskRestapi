import React from 'react';
import {Link, Router} from '@reach/router';


export const ComponentA = () => <h3>I am from component A</h3>
export const ComponentB = () => <h3>I am from component B</h3>

const About = props => {
    return (
        <div>
            <h2>I'm aobut page</h2>
            <Link to="/">Homepage</Link> <br />
            <Link to="a">Component A</Link> <br />
            <Link to="b">Component B</Link>
            
            <Router>
                <ComponentA path="a" default />
                <ComponentB path="b" />
            </Router>

        </div>
    );
}

export default About;
