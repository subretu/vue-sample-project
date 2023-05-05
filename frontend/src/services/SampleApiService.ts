import http from "@/http-common";

class SampleApiService {
  /* eslint @typescript-eslint/no-explicit-any: 0 */
  get(): Promise<any> {
    return http.get("/day");
  }

  delete(id: any): Promise<any> {
    return http.get(`/delete/${id}`);
  }

  insert(data: any): Promise<any> {
    return http.post("/insertdata", data);
  }

  task(is_button: any): Promise<any> {
    return http.get(`/task/${is_button}`);
  }

  get_json(): Promise<any> {
    return http.get("/jsondata");
  }

  get_member_name(id: any): Promise<any> {
    return http.get(`/get_member/${id}`);
  }
}

export default new SampleApiService();
