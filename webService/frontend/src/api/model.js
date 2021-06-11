import { reqGet, reqPost } from "./index.js";

export const runModel = async data => {
  return await reqPost("/model/run", data);
};
