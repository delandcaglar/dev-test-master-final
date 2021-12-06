import {
  Button,
  Card,
  CardContent,
  CardHeader,
  TextField,
} from "@material-ui/core";
import { useEffect, useState } from "react";
import * as settings from "../settings";
import axios from "axios";


export const Seller = ({ sellerId }: { sellerId: string }) => {
  interface CreateProps {
    old_handle: string;
  }
  const [seller, setSeller] = useState<{
    id: number;
    name: string;
    handle: string;
  } | null>(null);
  const [fetchSellerError, setFetchSellerError] = useState<string | null>(null);
  const [formData,setFormData] = useState<CreateProps>({
    old_handle: ""
});
  const{old_handle} = formData;
  const onChange =(event:any) =>{
    event.preventDefault();
    setFormData({...formData,[event.target.name]:event.target.value})
  }
  useEffect(() => {
    fetch(`${settings.API_SERVER}/api/sellers/${sellerId}`)
      .then(async (res) => {
        if (!res.ok) throw new Error("Failed to fetch seller");
        const data = await res.json();
        setSeller(data);
      })
      .catch((err) => {
        setFetchSellerError(err.message);
      });
  }, [sellerId]);

  if (fetchSellerError) {
    return <div>{fetchSellerError}</div>;
  }

  if (!seller) {
    return <div>pending</div>;
  }

  const handleSubmit = (event : any) => {
    event.preventDefault();
    console.log("old_handle", old_handle, seller.name, seller.id)
    let name_1 = seller.name
    let seller_1 = seller.id
    let handle_1 = seller.handle
    const config = {
      headers: {
        'Content-Type': 'application/json',

      }
    };
    const final = axios.put(`${settings.API_SERVER}/api/sellers/${seller_1}/`, {"name":name_1,"handle":old_handle}, config).then((response: any)=>{
      if (response.data.cannot_be_done !== "cannot_be_done"){
        axios.post(`${settings.API_SERVER}/api/sellers/handle/`, {"seller":seller_1,"old_handle":handle_1,"name":name_1}, config)
            .then((response: any)=>{
              window.location.reload()
              alert("updated")
            })
      }
      else{
        alert("link is already available")
      }
    })
  }
  return (
    <Card>
      <CardHeader title="Edit seller" subheader="Make changes to a seller" />
      <CardContent>
        <form noValidate onSubmit={handleSubmit} autoComplete="off">
          <TextField
            id="sellerId"
            label="Seller ID"
            fullWidth={true}
            style={{ margin: 8 }}
            name = "seller"
            value={seller.id}
            disabled={true}
          />
          <TextField
            id="sellerName"
            label="Seller Name"
            name ="name"
            fullWidth={true}
            style={{ margin: 8 }}
            value={seller.name}
            disabled={true}
          />
          <TextField
            id="sellerHandle"
            name="old_handle"
            label={seller.handle}
            fullWidth={true}
            onChange={onChange}
            style={{ margin: 8 }}
            value={old_handle}
          />
          <Button type="submit" variant="contained" color="primary">
            Update
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};
