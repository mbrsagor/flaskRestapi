import React from 'react';
import { Grid } from '@material-ui/core';

import Sidebar from './sidebar';
import Header from './header';
import Footer from './footer';


const Layout = props => {

    return (
        <div style={{width: '1140px', margin: '0 auto'}}>
            <Header />
            <Grid container spacing={3} justify="center">
            <Grid item xs={12} md={4}>
                <Sidebar />
            </Grid>
            <Grid item xs={12} md={8}>
                {props.children}
            </Grid>
            </Grid>
            <Footer />
        </div>
    )

}

export default Layout;
