import{useState} from 'react';
import './App.css';

const Person=()=>{
  return (
     <>
      <h1>Name: John</h1>
      <h2>Last Name: Doe</h2>
      <h2>Age: 30</h2>
     </>
  )}
  const App=()=>{
    const name='John';
    const isNameShowing = true;
    const isNameShows = false;
    const saw=null;
    const poo="Anna";
    const isUserLoggedIN=true;
    const [counter , setcounter] = useState(0);
    return (
     <div className="App">
      <h1>Hello, React!</h1>
      <h1>Hello, JSM!</h1>
      <h1>Hello, {name}! </h1>
      <h1>Hello, {isNameShowing ? name: 'someone'}!</h1>
      <h1>Hello, {isNameShows ? name: 'someone'}!</h1>
      <h1>Hello, {2 + 2}</h1>
      {saw ? (
        <>
         test
        </>
      ): (
        <>
          <h1>test</h1>
          <h2>There is a no name</h2>
        </>
      )}
      {poo ? (
        <>
         <h1>{poo}</h1>
        </>
      ): (
        <>
          <h1>test</h1>
          <h2>There is a no name</h2>
        </>
      )}
      <Person/>
      <>
      <button onClick={()=> setcounter((prevCount) => prevCount -1)}>-</button>
      <h1>{counter}</h1>
      <button onClick={()=> setcounter((prevCount) => prevCount +1)}>+</button>
      </>
    </div>
    );
  }
export default App;