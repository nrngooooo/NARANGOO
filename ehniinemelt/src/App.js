import './App.css';
import { useState } from 'react';

const App = () => {
  const [time, setTime] = useState(0);

  const getTime = () => {
    fetch('http://utils.mandakh.org:8000/utils/', {
      method: "POST",
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify({
        action: "gettime"
      }),
    })
      .then((resp) => resp.json())
      .then((data) => {
        setTime(data["data"]["time"]);
      })
      .catch((err) => {
        console.log(err.message);
      })
  }
  return (
    <div>
      <button className="py-3 px-6 sm:w-[60%] my-4" onClick={() => { getTime() }}>Click on button</button>
      <div className='time'>{time}</div>
    </div>
  )
}
export default App;
