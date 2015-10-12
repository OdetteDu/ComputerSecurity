package com.cs155.trustedapp;

import android.app.IntentService;
import android.content.ContentResolver;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.os.ResultReceiver;
import android.provider.ContactsContract.Contacts;

public class ReadContactsService
  extends IntentService
{
  protected static final String CONTACTS_STRING_KEY = "CONTACTS_STRING_KEY";
  protected static final String REQUEST_CONTACTS_STRING = "REQUEST_CONTACTS_STRING";
  public static final int RESULT_ID_CONTACTS = 1;
  private final String ACTUAL_SECRET_KEY = "youllnevergetmeluckycharms";
  private IGetContactsString.Stub icontacts_sub = new IGetContactsString.Stub()
  {
    public String GetContacts(String paramAnonymousString)
      throws RemoteException
    {
      return ReadContactsService.this.safeRetrieveContacts(paramAnonymousString);
    }
  };
  
  public ReadContactsService()
  {
    super("BLANK_CONSTRUCTOR_CALLED");
  }
  
  public ReadContactsService(String paramString)
  {
    super(paramString);
  }
  
  private Cursor getContacts()
  {
    Uri localUri = ContactsContract.Contacts.CONTENT_URI;
    return getContentResolver().query(localUri, new String[] { "_id", "display_name" }, "in_visible_group = '1'", null, "display_name COLLATE LOCALIZED ASC");
  }
  
  private String safeRetrieveContacts(String paramString)
  {
    if ((paramString == null) || (paramString.length() == 0)) {
      return "";
    }
    if (strcmp(paramString, "youllnevergetmeluckycharms")) {
      return retrieveContacts();
    }
    return "";
  }
  
  private boolean strcmp(String paramString1, String paramString2)
  {
    int i = 0;
    for (;;)
    {
      if ((i >= paramString1.length()) || (i >= paramString2.length())) {
        return true;
      }
      if (paramString1.charAt(i) != paramString2.charAt(i)) {
        return false;
      }
      i += 1;
    }
  }
  
  public IBinder onBind(Intent paramIntent)
  {
    return this.icontacts_sub;
  }
  
  protected void onHandleIntent(Intent paramIntent)
  {
    String str = safeRetrieveContacts(paramIntent.getStringExtra("SECRET_KEY"));
    paramIntent = (ResultReceiver)paramIntent.getParcelableExtra("REQUEST_CONTACTS_STRING");
    Bundle localBundle = new Bundle();
    localBundle.putString("CONTACTS_STRING_KEY", str);
    paramIntent.send(1, localBundle);
  }
  
  public int onStartCommand(Intent paramIntent, int paramInt1, int paramInt2)
  {
    return super.onStartCommand(paramIntent, paramInt1, paramInt2);
  }
  
  public String retrieveContacts()
  {
    String str1 = new String();
    Cursor localCursor = getContacts();
    for (;;)
    {
      if (!localCursor.moveToNext()) {
        return str1;
      }
      String str2 = localCursor.getString(localCursor.getColumnIndex("display_name"));
      str1 = str1 + "Name: " + str2 + "\n";
    }
  }
}
