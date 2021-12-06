import {
  Button,
  Card,
  CardContent,
  CardHeader,
  InputAdornment,
  TextField,
} from "@material-ui/core";
import { useEffect, useState } from "react";
import * as settings from "../settings";

export const PaySeller = ({ sellerHandle }: { sellerHandle: string }) => {
  const [sellerName, setSellerName] = useState<string | null>(null);
  const [fetchSellerError, setFetchSellerError] = useState<string | null>(null);

  useEffect(() => {
    fetch(`${settings.API_SERVER}/api/sellers/handle/${sellerHandle}`)
      .then(async (res) => {
        if (!res.ok) throw new Error("Failed to fetch seller");

        const data = await res.json();
        setSellerName(data.name);
      })
      .catch((err) => {

        setFetchSellerError(err.message);
      });
  }, [sellerHandle]);

  if (fetchSellerError) {
    return <div>{fetchSellerError}</div>;
  }

  if (!sellerName) {
    return <div>pending</div>;
  }

  return (
    <Card>
      <CardHeader
        title="Payment Details"
        subheader={`Start by entering a reference and amount for your payment to ${sellerName}.`}
      />
      <CardContent>
        <form noValidate autoComplete="off">
          <TextField
            id="amount"
            label="Amount"
            placeholder="149.99"
            fullWidth={true}
            style={{ margin: 8 }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">£</InputAdornment>
              ),
            }}
          />
          <TextField
            id="reference"
            label="Reference"
            placeholder="Invoice #123"
            fullWidth={true}
            style={{ margin: 8 }}
          />
          <Button variant="contained" color="primary">
            Secure Checkout
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};
