import React, { useEffect, useState } from 'react';

function App() {
  const [joke, setJoke] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/joke')
      .then(res => res.json())
      .then(data => setJoke(data.joke))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Random Joke</h1>
      <p>{joke || 'Loading...'}</p>
    </div>
  );
}

export default App;