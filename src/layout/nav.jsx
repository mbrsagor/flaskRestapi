import React from 'react';
import { Link } from '@reach/router';

const Nav = () => {

    return (
        <div>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About US</Link></li>
            </ul>
        </div>
    )

}

export default Nav;
