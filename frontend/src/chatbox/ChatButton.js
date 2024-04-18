import React, { useState } from 'react';
import '../App.css';
import { Avatar } from '@mui/material';
import { Chat } from '@mui/icons-material'; 
import CloseIcon from '@mui/icons-material/Close';

const ChatButton = ({ onClick }) => {
  const [chatOpen, setChatOpen] = useState(false);

  const toggleIcon = () => {
    onClick();
    setChatOpen(!chatOpen);
  }
  return (
    <Avatar 
    onClick={toggleIcon}
    sx={{
      bgcolor: '#00C895',
      width: '70px',
      height: '70px',
      border: '2px solid grey',
      position: "fixed",
      bottom: "20px",
      right: "20px",
      '&:hover': {
        cursor: 'pointer',
        bgcolor: "#00CE9A"
      }}}>
        {chatOpen ? <CloseIcon sx={{ fontSize: '3.2rem' }}/> : <Chat sx={{ fontSize: '2rem' }}/> }
      </Avatar>
  );
};

export default ChatButton;