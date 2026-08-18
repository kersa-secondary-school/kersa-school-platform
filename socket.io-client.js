import { useEffect, useRef } from 'react';
import { io } from 'socket.io-client';

const socket = io('ws://localhost:8000', { auth: { token: localStorage.getItem('access_token') } });

socket.on('chat_message', (data) => {
  console.log('New message', data);
});