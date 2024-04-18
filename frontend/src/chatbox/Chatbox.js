import React, { useState, useRef } from "react";
import ScrollToBottom from "react-scroll-to-bottom";
import StraightIcon from '@mui/icons-material/Straight';

const Chatbox = ({ isOpen }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const scrollRef = useRef();

  const sendMessage = async (event) => {
    event.preventDefault();
    if (input) {
      setMessages([...messages, { text: input, sender: "user" }]);
      setInput("");
      try {
        const response = await fetch("http://127.0.0.1:5000", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ input }),
        });
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        // Assume your backend responds with a message property
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: data.message, sender: "bot" },
        ]);
      } catch (error) {
        console.error("Error sending message:", error);
      }
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
