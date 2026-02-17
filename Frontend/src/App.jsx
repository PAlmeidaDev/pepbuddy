import { useEffect, useState } from 'react'
import './index.css'

function App() {
  const [meds, setMeds] = useState([])

  const fetchMeds = () => {
    fetch('http://127.0.0.1:8000/api/medications/')
      .then(res => res.json())
      .then(data => setMeds(data))
  }

  useEffect(() => {
    fetchMeds()
  }, [])

  const handleLogDose = (id) => {
    fetch(`http://127.0.0.1:8000/api/medications/${id}/log_dose/`, {
      method: 'POST',
    })
    .then(res => {
      if (res.ok) {
        fetchMeds() // Refresh the data to show the new stock/time
      }
    })
  }

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-blue-900 mb-8">PepBuddy Dashboard</h1>

        <div className="grid gap-6 md:grid-cols-2">
          {meds.map(m => (
            <div key={m.id} className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
              <div className="flex justify-between items-start mb-4">
                <h2 className="text-xl font-semibold text-gray-800">{m.name}</h2>
                <span className="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded">
                  {m.dosage_qnt}mg
                </span>
              </div>

              <div className="space-y-2 mb-6">
                <p className="text-sm text-gray-600">Stock: <span className="font-bold">{m.current_stock}</span></p>
                <p className="text-sm text-gray-600">Next Dose: <span className="font-medium text-blue-600">
                  {new Date(m.next_dose).toLocaleString()}
                </span></p>
              </div>

              <button
                onClick={() => handleLogDose(m.id)}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg transition duration-200"
              >
                Log Dose
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App