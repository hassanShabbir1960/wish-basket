import './App.css';
import ProductsList from './components/ProductsList';

import Container from '@mui/material/Container';

function App() {
  return (
    <div className="App">
      <header className="App-header">
       
      <Container>
          <ProductsList></ProductsList>
      </Container>
        
      </header>
    </div>
  );
}

export default App;
