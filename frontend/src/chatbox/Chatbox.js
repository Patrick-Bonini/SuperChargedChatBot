import React, { useState, useRef } from "react";
import ScrollToBottom from "react-scroll-to-bottom";
import StraightIcon from '@mui/icons-material/Straight';

const Chatbox = ({ isOpen }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const scrollRef = useRef();
  const sendMessage = (event) => {
    event.preventDefault();
    if (input) {
      setMessages([...messages, { text: input, sender: "user" }]);
      setInput("");
      // Here you can add the code to send the message to your chatbot and get the response
      // For now, we'll just echo the user's message
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: input, sender: "bot" },
      ]);
    }
  };

  return (
    isOpen && (
      <div className={`chatbox ${isOpen ? "open" : ""}`}>
        <ScrollToBottom
          className="message-container"
          scrollViewClassName="messages"
          ref={scrollRef}
        >
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              {message.text}
            </div>
          ))}
        </ScrollToBottom>
        <form className="message-form" onSubmit={sendMessage}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Message Solly..."
          />
          <button type="submit" style={{backgroundColor: "#00C895", borderRadius: "10px", padding: "0px 8px 0px 8px"}}><StraightIcon sx={{ fontSize: '1.3rem' }}/></button>
        </form>
      </div>
    )
  );
};

export default Chatbox;
