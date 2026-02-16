import { useEffect, useState } from 'react'

function App() {
  const [meds, setMeds] = useState([])

  useEffect(() => {
    // This is the call to your Django API
    fetch('http://127.0.0.1:8000/api/medications/')
      .then(response => response.json())
      .then(data => setMeds(data))
      .catch(err => console.error("Error fetching meds:", err))
  }, [])

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>PepBuddy Dashboard</h1>
      <ul>
        {meds.map(m => (
          <li key={m.id}>
            <strong>{m.name}</strong> - Stock: {m.current_stock}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App