import React from 'react';
import { Router } from '@reach/router';

import Layout from '../layout';
import Home from '../pages/home';
import About from '../pages/about';

const PageNotFound = () => <h2>Sorry! Page not found</h2>

function App() {
  return (
    <Layout>
      <Router>
          <Home path="/" />
          <About path="/about/*" />
          <PageNotFound default/>
      </Router>
    </Layout>
  );
}

export default App;
