// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


// import ReactDOM from "react-dom/client";
// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import React from 'react';
// import ScannerPage from './ScannerPage';
// import Chatbot from './Chatbot';
// import './App.css'; // Import global styles if needed

// const App = () => {
//   return (
//     <div className="app-container">
//       <ScannerPage />
//     </div>
//   );
// };

// export default App;





// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import ScannerPage from './ScannerPage';
// import Chatbot from './Chatbot';

// function App() {
//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<ScannerPage />} />
//         <Route path="/chatbot" element={<Chatbot />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;



import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react';
import ScannerPage from './ScannerPage';
import Chatbot from './Chatbot';
import './App.css'; // Import global styles if needed

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ScannerPage />}/>
          
        <Route path="/chatbot" element={<Chatbot />} />
        
      </Routes>
    </BrowserRouter>
  );
};

export default App;