// import React, { Component } from 'react'
// import QrReader from 'react-qr-scanner'

// class ScannerPage extends Component {
//   constructor(props){
//     super(props)
//     this.state = {
//       delay: 100,
//       result: 'No result',
//     }

//     this.handleScan = this.handleScan.bind(this)
//   }

//   handleScan(data){
//     this.setState({
//       result: data,
//     })
//   }
//   handleError(err){
//     console.error(err)
//   }
//   render(){
//     const previewStyle = {
//       height: 240,
//       width: 320,
//     }

//     return(
//       <div>
//         <QrReader
//           delay={this.state.delay}
//           style={previewStyle}
//           onError={this.handleError}
//           onScan={this.handleScan}
//           />
//         <p>{this.state.result}</p>
//       </div>
//     )
//   }
// }
// export default ScannerPage;





// import React, { Component } from 'react';
// import QrReader from 'react-qr-scanner';

// class ScannerPage extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       delay: 100,
//       result: 'No result',
//     }

//     this.handleScan = this.handleScan.bind(this);
//   }

//   handleScan(data) {
//     if (data) {
//       this.setState({
//         result: data.text, // Extract text property from the QR code result object
//       });
  
//       // Optionally, you can also send this data to your backend here
//       this.sendQRData(data.text);
//     }
//   }
  

//   handleError(err) {
//     console.error(err);
//   }

//   sendQRData(data) {
//     const apiUrl = `http://localhost:8000/roomno/${data}`;
  
//     fetch(apiUrl, {
//       method: 'GET',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//     .then(response => response.json())
//     .then(data => {
//       console.log('Success:', data);
//       // Handle response from backend if needed
//       this.setState({
//         result: data.result, // Assuming backend returns result in JSON response
//       });
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
//   }
  

//   render() {
//     const previewStyle = {
//       height: 240,
//       width: 320,
//     }

//     return (
//       <div>
//         <QrReader
//           delay={this.state.delay}
//           style={previewStyle}
//           onError={this.handleError}
//           onScan={this.handleScan}
//         />
//         <p>{this.state.result}</p>
//       </div>
//     )
//   }
// }

// export default ScannerPage;






// import React, { useState } from 'react';
// import QrReader from 'react-qr-scanner';
// import { useNavigate } from 'react-router-dom';

// const ScannerPage = () => {
//   const navigate = useNavigate();
//   const [result, setResult] = useState('No result');

//   const handleScan = (data) => {
//     if (data) {
//       setResult(data.text); // Update result state with QR code text
//       sendQRData(data.text); // Send QR code text to backend
//     }
//   }

//   const handleError = (err) => {
//     console.error(err);
//   }

//   const sendQRData = (data) => {
//     fetch(`http://localhost:8000/roomno/${data}`)
//       .then(response => response.json())
//       .then(data => {
//         console.log('Success:', data);
//         // Assuming data from backend contains necessary details or confirmation
//         navigate('/chatbot'); // Navigate to the Chatbot route
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   }

//   const previewStyle = {
//     height: 240,
//     width: 320,
//   }

//   return (
//     <div>
//       <QrReader
//         delay={100}
//         style={previewStyle}
//         onError={handleError}
//         onScan={handleScan}
//       />
//       <p>{result}</p>
//     </div>
//   );
// };

// export default ScannerPage;










// import React, { useState } from 'react';
// import QrReader from 'react-qr-scanner';
// import { useNavigate } from 'react-router-dom';

// const ScannerPage = () => {
//   const navigate = useNavigate();
//   const [result, setResult] = useState('No result');

//   const handleScan = (data) => {
//     if (data) {
//       setResult(data.text);
//       sendQRData(data.text);
//     }
//   }

//   const handleError = (err) => {
//     console.error(err);
//   }

//   const sendQRData = (data) => {
//     fetch(`http://localhost:8000/roomno/${data}`)
//       .then(response => response.json())
//       .then(data => {
//         console.log('Success:', data);
//         // Navigate to the Chatbot route with the scanned data
//         navigate('/chatbot', { 
//           state: { 
//             roomNo: data.roomNo,
//             firstName: data.firstName,
//             bookingId: data.bookingId
//           } 
//         });
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   }

//   const previewStyle = {
//     height: 240,
//     width: 320,
//   }

//   return (
//     <div>
//       <QrReader
//         delay={100}
//         style={previewStyle}
//         onError={handleError}
//         onScan={handleScan}
//       />
//       <p>{result}</p>
//     </div>
//   );
// };

// export default ScannerPage;








// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react';
// eslint-disable-next-line no-unused-vars
import QrReader from 'react-qr-scanner';
import { useNavigate } from 'react-router-dom';

const ScannerPage = () => {
  const navigate = useNavigate();
  // eslint-disable-next-line no-unused-vars
  const [result, setResult] = useState('No result');

  // eslint-disable-next-line no-unused-vars
  const handleScan = (data) => {
    if (data) {
      setResult(data.text);
      sendQRData(data.text);
    }
  }

  // eslint-disable-next-line no-unused-vars
  const handleError = (err) => {
    console.error(err);
  }

  const sendQRData = (data) => {
    fetch(`http://localhost:8000/roomno/${data}`)
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        // Store the data in window.log
        window.log = {
          roomno: data.roomno,
          firstname: data.firstname,
          Booking_id: data.Booking_id
        };
        // Navigate to the Chatbot route
        navigate('/chatbot');
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  const previewStyle = {
    height: 240,
    width: 320,
  }

  return (
    <div>
      <QrReader
        delay={100}
        style={previewStyle}
        onError={handleError}
        onScan={handleScan}
      />
      <p>{result}</p>
    </div>
  );
};

export default ScannerPage;