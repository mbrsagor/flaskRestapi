import React from 'react';
import {Grid, Typography} from '@material-ui/core';


function App() {
  return (
    <Grid container>
      <Grid md={6} spacing={4}>
        <Typography variant="h4" align="center">
            Material UI is a awesome
          </Typography>
      </Grid>
    </Grid>
  );
}

export default App;
