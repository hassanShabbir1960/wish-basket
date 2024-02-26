import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';
import Grid from '@mui/material/Grid';

function ProductsList() {
  const [products, setProducts] = useState([]); // Initialize state to hold products

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/products'); // Use your API endpoint here
        setProducts(response.data.products); // Update state with fetched products
        console.log(response.data.products)
      } catch (error) {
        console.error("Error fetching data: ", error);
        // Handle error here, e.g., set error state, show message, etc.
      }
    };

    fetchProducts(); // Call the function to fetch products
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <Grid container spacing={1}>
      {products.map((product, index) => (
        <Grid item xs={12} sm={6} md={4} key={index} >
          <ProductCard
            productName={product.name}
            price={product.price}
            category={product.category}
            imageBytes={product.image}
          />
        </Grid>
      ))}
    </Grid>
  );
}

export default ProductsList;
