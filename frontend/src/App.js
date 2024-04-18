import React, { useState, useRef } from 'react';
import ScrollToBottom from 'react-scroll-to-bottom';
import './App.css';
import ChatButton from './chatbox/ChatButton';
import Chatbox from './chatbox/Chatbox';

function App() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleChatbox = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="App">
      <ChatButton onClick={toggleChatbox} />
      <Chatbox isOpen={isOpen} />
    </div>
  );
}

export default App;

// function App() {
//   const [messages, setMessages] = useState([]);
//   const [input, setInput] = useState('');
//   const scrollRef = useRef();

//   const sendMessage = (event) => {
//     event.preventDefault();
//     if (input) {
//       setMessages([...messages, { text: input, sender: 'user' }]);
//       setInput('');
//       // Here you can add the code to send the message to your chatbot and get the response
//       // For now, we'll just echo the user's message
//       setMessages((prevMessages) => [...prevMessages, { text: input, sender: 'bot' }]);
//     }
//   };

//   return (
//     <div className="App">
//       <ScrollToBottom className="message-container" scrollViewClassName="messages" ref={scrollRef}>
//         {messages.map((message, index) => (
//           <div key={index} className={`message ${message.sender}`}>
//             {message.text}
//           </div>
//         ))}
//       </ScrollToBottom>
//       <form className="message-form" onSubmit={sendMessage}>
//         <input
//           type="text"
//           value={input}
//           onChange={(e) => setInput(e.target.value)}
//           placeholder="Type your message..."
//         />
//         <button type="submit">Send</button>
//       </form>
//     </div>
//   );
// }

// export default App;