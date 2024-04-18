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