import http from "@/http-common";

class SampleApiService {
  /* eslint @typescript-eslint/no-explicit-any: 0 */
  get(): Promise<any> {
    return http.get("/day");
  }

  delete(id: any): Promise<any> {
    return http.get(`/delete/${id}`);
  }
}

export default new SampleApiService();
