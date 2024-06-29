// import React, { useState, useRef, useEffect } from 'react';
// import './Chatbot.css'; // Import CSS file for styling

// const Chatbot = () => {
//   const [messages, setMessages] = useState([
//     { text: 'Hello! How can I assist you today?', isBot: true }
//   ]);
//   const [inputValue, setInputValue] = useState('');
//   const messagesEndRef = useRef(null);

//   // Function to handle sending a message
//   const handleSendMessage = () => {
//     if (inputValue.trim() === '') return;

//     const newMessage = { text: inputValue, isBot: false };
//     setMessages(prevMessages => [...prevMessages, newMessage]);
//     setInputValue('');

//     // Simulate bot response (replace with actual backend call in real application)
//     setTimeout(() => {
//       const botResponse = { text: 'I received your message: ' + inputValue, isBot: true };
//       setMessages(prevMessages => [...prevMessages, botResponse]);
//     }, 500);
//   };

//   // Effect to scroll messages to the bottom when new message arrives
//   useEffect(() => {
//     if (messagesEndRef.current) {
//       messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
//     }
//   }, [messages]);

//   return (
//     <div className="chatbot-container">
//       <div className="chatbot-header">
//         <h1>Chatbot</h1>
//       </div>
//       <div className="messages-container">
//         {messages.map((message, index) => (
//           <div key={index} className={`message ${message.isBot ? 'bot' : 'user'}`}>
//             <div className="message-text">{message.text}</div>
//           </div>
//         ))}
//         <div ref={messagesEndRef} /> {/* Ref to scroll to bottom */}
//       </div>
//       <div className="input-container">
//         <input
//           type="text"
//           value={inputValue}
//           onChange={(e) => setInputValue(e.target.value)}
//           placeholder="Type your message..."
//         />
//         <button onClick={handleSendMessage}>Send</button>
//       </div>
//     </div>
//   );
// };

// export default Chatbot;









// import React, { useState, useRef, useEffect } from 'react';
// import './Chatbot.css'; // Import CSS file for styling

// const Chatbot = () => {
//   const [messages, setMessages] = useState([
//     { text: 'Hello! How can I assist you today?', isBot: true }
//   ]);
//   const [inputValue, setInputValue] = useState('');
//   const messagesEndRef = useRef(null);

//   // Function to handle sending a message
//   const handleSendMessage = () => {
//     if (inputValue.trim() === '') return;

//     const newMessage = { text: inputValue, isBot: false };
//     setMessages(prevMessages => [...prevMessages, newMessage]);
//     setInputValue('');

//     // Simulate bot response (replace with actual backend call in real application)
//     setTimeout(() => {
//       const botResponse = { text: 'I received your message: ' + inputValue, isBot: true };
//       setMessages(prevMessages => [...prevMessages, botResponse]);
//     }, 500);
//   };

//   // Effect to scroll messages to the bottom when new message arrives
//   useEffect(() => {
//     if (messagesEndRef.current) {
//       messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
//     }
//   }, [messages]);

//   return (
//     <div className="chatbot-container">
//       <div className="chatbot-header">
//         <h1>Chatbot</h1>
//       </div>
//       <div className="messages-container">
//         {messages.map((message, index) => (
//           <div key={index} className={`message ${message.isBot ? 'bot' : 'user'}`}>
//             <div className="message-text">{message.text}</div>
//           </div>
//         ))}
//         <div ref={messagesEndRef} /> {/* Ref to scroll to bottom */}
//       </div>
//       <div className="input-container">
//         <input
//           type="text"
//           value={inputValue}
//           onChange={(e) => setInputValue(e.target.value)}
//           placeholder="Type your message..."
//         />
//         <button onClick={handleSendMessage}>Send</button>
//       </div>
//     </div>
//   );
// };

// export default Chatbot;




// import React, { useState, useRef, useEffect } from 'react';
// import axios from 'axios';
// import './Chatbot.css';

// const Chatbot = () => {
//   const [messages, setMessages] = useState([
//     { text: 'Hello! How can I assist you today?', isBot: true }
//   ]);
//   const [inputValue, setInputValue] = useState('');
//   const messagesEndRef = useRef(null);

//   const handleSendMessage = async () => {
//     if (inputValue.trim() === '') return;

//     let roomNumber = '123'; // Replace with actual room number
//     let bookId = 'ABC123'; // Replace with actual book ID

//     const newMessage = { text: inputValue, isBot: false };
//     setMessages(prevMessages => [...prevMessages, newMessage]);
//     setInputValue('');

//     try {
//       const payload = {
//         room: roomNumber,
//         book_id: bookId,
//         message: inputValue
//       };

//       const encodedPayload = encodeURIComponent(JSON.stringify(payload));
//       const response = await axios.get(`http://localhost:8000/process_query/${encodedPayload}`);

//       const botResponse = { text: response.data.message, isBot: true };
//       setMessages(prevMessages => [...prevMessages, botResponse]);
//     } catch (error) {
//       console.error('Error sending message:', error);
//       const errorMessage = 'Sorry, there was an error processing your message.';
//       const errorBotResponse = { text: errorMessage, isBot: true };
//       setMessages(prevMessages => [...prevMessages, errorBotResponse]);
//     }
//   };

//   useEffect(() => {
//     if (messagesEndRef.current) {
//       messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
//     }
//   }, [messages]);

//   return (
//     <div className="chatbot-container">
//       <div className="chatbot-header">
//         <h1>Chatbot</h1>
//       </div>
//       <div className="messages-container">
//         {messages.map((message, index) => (
//           <div key={index} className={`message ${message.isBot ? 'bot' : 'user'}`}>
//             <div className="message-text">{message.text}</div>
//           </div>
//         ))}
//         <div ref={messagesEndRef} />
//       </div>
//       <div className="input-container">
//         <input
//           type="text"
//           value={inputValue}
//           onChange={(e) => setInputValue(e.target.value)}
//           placeholder="Type your message..."
//           onKeyPress={(e) => {
//             if (e.key === 'Enter') {
//               handleSendMessage();
//             }
//           }}
//         />
//         <button onClick={handleSendMessage}>Send</button>
//       </div>
//     </div>
//   );
// };

// export default Chatbot;



import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './Chatbot.css';
import { useNavigate } from 'react-router-dom';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const messagesEndRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!window.log || !window.log.roomno || !window.log.Booking_id || !window.log.firstname) {
      console.error('Required data not found. Please scan QR code first.');
      navigate('/');  // Navigate to the home page or scanner page
      return;
    }

    const welcomeMessage = `Hello, ${window.log.firstname}! Welcome to room ${window.log.roomno}. How can I assist you today?`;
    setMessages([{ text: welcomeMessage, isBot: true }]);
  }, [navigate]);

  const handleSendMessage = async () => {
    if (inputValue.trim() === '') return;

    const newMessage = { text: inputValue, isBot: false };
    setMessages(prevMessages => [...prevMessages, newMessage]);
    setInputValue('');

    try {
      const payload = {
        room: window.log.roomno,
        book_id: window.log.Booking_id,
        message: inputValue
      };

      const encodedPayload = encodeURIComponent(JSON.stringify(payload));
      const response = await axios.get(`http://localhost:8000/process_query/${encodedPayload}`);

      const botResponse = { text: response.data.message, isBot: true };
      setMessages(prevMessages => [...prevMessages, botResponse]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = 'Sorry, there was an error processing your message.';
      const errorBotResponse = { text: errorMessage, isBot: true };
      setMessages(prevMessages => [...prevMessages, errorBotResponse]);
    }
  };

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <h1>Chatbot</h1>
      </div>
      <div className="messages-container">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.isBot ? 'bot' : 'user'}`}>
            <div className="message-text">{message.text}</div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="input-container">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your message..."
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              handleSendMessage();
            }
          }}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;