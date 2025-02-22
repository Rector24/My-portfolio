using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;
using System.Xml.Linq;
using System.Data.SqlClient;

namespace aVISTO
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection connection = new SqlConnection(@"Data Source=DESKTOP-2LP800J\SQLEXPRESS;Initial Catalog=BCExam;Integrated Security=True");
        SqlCommand command;
        int usernameCheck(string Snum)
        {
            connection.Open();
            string query = "SELECT COUNT(*) FROM RegistrationTBL where Snum='" + Snum+ "'";
            SqlCommand command = new SqlCommand(query, connection);
            int v = (int)command.ExecuteScalar();
            connection.Close();
            return v;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {

                if (Snum.Text != "" && Fname.Text != "" && DOB.Text != "" && address.Text != "")
                {
                    int v = usernameCheck(Snum.Text);
                    if (v != 1)
                    {
                        connection.Open();
                        string query = "INSERT INTO RegistrationTBL(Snum,Fname,DOB,address,gender,Phone,Modul,password) values(@Snum,@Fname,@DOB,@address,@gender,@Phone,@Modul,@password)";
                        command = new SqlCommand(query, connection);
                        command.Parameters.AddWithValue("@Snum", Snum.Text);
                        command.Parameters.AddWithValue("@Fname", Fname.Text);
                        command.Parameters.AddWithValue("@DOB",Convert.ToDateTime( DOB.Text));
                        command.Parameters.AddWithValue("@address", address.Text);
                        command.Parameters.AddWithValue("@gender", gender.Text);
                        command.Parameters.AddWithValue("@Phone", Phone.Text);
                        command.Parameters.AddWithValue("@Modul", Modul.Text);
                        command.Parameters.AddWithValue("@password", password.Text);
                        command.ExecuteNonQuery();
                        connection.Close();
                        MessageBox.Show("You have successfully registered!");
                           Snum.Text = "";
                            Fname.Text = "";
                        DOB.Text = "";
                        address.Text = "";
                        gender.Text = "";
                        Phone.Text = "";
                        Modul.Text = "";
                        password.Text = "";


                    }
                    else
                    {
                        MessageBox.Show("Username is available !!!!");
                    }
                }
                else
                {
                    MessageBox.Show("Fill in the fields!!!");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            this.Hide(); 
            Login login = new Login();
            
            login.Show();
        }
    }

 }

