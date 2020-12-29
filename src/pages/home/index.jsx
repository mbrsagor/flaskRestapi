import React from 'react';
import {Link} from '@reach/router';

const Home = () => {
    return (
        <div>
            <h2>I'm aobut Homepage</h2>
            <Link to="/about">About</Link>
        </div>
    );
}

export default Home;
