import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly accessTokenKey = 'portfolio_access_token';
  private readonly refreshTokenKey = 'portfolio_refresh_token';

  getAccessToken(): string | null {
    try {
      return localStorage.getItem(this.accessTokenKey);
    } catch {
      return null;
    }
  }

  setTokens(accessToken: string, refreshToken?: string): void {
    try {
      localStorage.setItem(this.accessTokenKey, accessToken);
      if (refreshToken) localStorage.setItem(this.refreshTokenKey, refreshToken);
    } catch {
      // ignore storage errors (private mode etc.)
    }
  }

  clearTokens(): void {
    try {
      localStorage.removeItem(this.accessTokenKey);
      localStorage.removeItem(this.refreshTokenKey);
    } catch {
      // ignore
    }
  }

  isAuthenticated(): boolean {
    return !!this.getAccessToken();
  }
}

