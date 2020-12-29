import React from 'react';
import {Router} from '@reach/router';
import {Grid, Typography, Button} from '@material-ui/core';

import Home from '../pages/home';
import About, {ComponentA, ComponentB} from '../pages/about';

const PageNotFound = () => <h2>Sorry! Page not found</h2>

function App() {
  return (
    <Grid container justify="center">
      <Grid md={6} spacing={4}>
        <Typography variant="h4"> Material UI is a awesome</Typography>
        <Button variant="contained" color="primary" size="small">Learn More...</Button>
        <Router>
            <Home path="/" />
            <About path="about/*"/>
            <PageNotFound default />
        </Router>
      </Grid>
    </Grid>
  );
}

export default App;
