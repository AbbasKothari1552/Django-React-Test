import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api'; // Import the api instance

const Activate = () => {
    const { uid, token } = useParams();
    const [activated, setActivated] = useState(false);

    useEffect(() => {
        const verifyUser = async () => {
            try {
                await api.post('/auth/users/activation/', { uid, token }); // Use api instance here
                setActivated(true);
            } catch (error) {
                console.error('Error during activation:', error);
            }
        };
        verifyUser();
    }, [uid, token]);

    return (
        <div>
            {activated ? (
                <p>Your account has been activated successfully!</p>
            ) : (
                <p>Activating your account...</p>
            )}
        </div>
    );
};

export default Activate;
