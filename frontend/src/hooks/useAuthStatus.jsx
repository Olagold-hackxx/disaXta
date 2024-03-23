import React, { useEffect, useState } from "react";

export const useAuthStatus = () => {
  const [loggedIn, setLoggedIn] = useState(false);
  const [checkingStatus, setCheckingStatus] = useState(true);

  useEffect(() => {
    const auth = true
 
      if (auth) {
        
        setLoggedIn(true);
        
      }
      setCheckingStatus(false);
   
  }, []);
  return {loggedIn, checkingStatus};
};
